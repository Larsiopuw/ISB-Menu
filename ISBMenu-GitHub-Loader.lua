assert(type(loadstring)=="function", "Der Executor unterstützt loadstring nicht.")
local source=game:HttpGet("https://raw.githubusercontent.com/Larsiopuw/ISB-Menu/main/ISBMenu.lua")
local chunk,reason=loadstring(source,"ISBMenu")
assert(chunk,reason)
return chunk()
-- by Larsiopuw
