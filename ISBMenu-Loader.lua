-- Local loader. Place ISBMenu.lua in your executor's workspace folder.
assert(type(readfile) == "function", "Dieser Executor unterstützt readfile nicht. ISBMenu.lua direkt ausführen.")
assert(type(loadstring) == "function", "Dieser Executor unterstützt loadstring nicht.")
local source = readfile("ISBMenu.lua")
local chunk, reason = loadstring(source, "ISBMenu")
assert(chunk, reason)
return chunk()
-- by Larsiopuw
