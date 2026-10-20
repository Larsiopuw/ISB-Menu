-- Always resolve GitHub main freshly; no release version is pinned here.
assert(type(loadstring)=="function", "This executor does not support loadstring.")
local http=game:GetService("HttpService")
local raw="https://raw.githubusercontent.com/Larsiopuw/ISB-Menu/"
local function fresh(url)
    return game:HttpGet(url.."?isb="..http:GenerateGUID(false))
end
local resolved,sha=pcall(function()
    local ref=http:JSONDecode(fresh("https://api.github.com/repos/Larsiopuw/ISB-Menu/git/ref/heads/main"))
    local commit=ref and ref.object and ref.object.sha
    assert(ref.ref=="refs/heads/main" and type(commit)=="string" and #commit==40 and commit:match("^[%da-fA-F]+$"), "Invalid main reference.")
    return commit
end)
-- Public API rate limits must not prevent a fresh main download.
local ok,source=pcall(function()
    return fresh(raw..(resolved and sha or "refs/heads/main").."/ISBMenu.lua")
end)
assert(ok and type(source)=="string" and #source>0, "ISB Menu could not download GitHub main. Please try again.")
local chunk,reason=loadstring(source,"ISBMenu")
assert(chunk, "ISB Menu could not compile the downloaded script: "..tostring(reason))
return chunk()
-- by Larsiopuw
