-- Diagnostic loader: reports download, compilation and runtime errors separately.
assert(type(loadstring)=="function","ISB [Loader]: loadstring ist in diesem Executor nicht verfügbar.")
local ok,source=pcall(function()
    return game:HttpGet("https://raw.githubusercontent.com/Larsiopuw/ISB-Menu/main/ISBMenu.lua?release=2.6.4")
end)
assert(ok,"ISB [Download]: "..tostring(source))
assert(type(source)=="string" and source:find("ISB Menu",1,true),"ISB [Download]: Keine gültige Menüdatei erhalten.")
local compiled,chunk,reason=pcall(loadstring,source,"ISBMenu-2.6.4")
assert(compiled,"ISB [Compiler]: "..tostring(chunk))
assert(type(chunk)=="function","ISB [Compiler]: "..tostring(reason or "Kein ausführbarer Code zurückgegeben."))
local function traceback(err)
    if type(debug)=="table" and type(debug.traceback)=="function" then
        return debug.traceback(tostring(err),2)
    end
    return tostring(err)
end
local started,result=xpcall(chunk,traceback)
assert(started,"ISB [Laufzeit]: "..tostring(result))
print("ISB 2.6.4: Start ohne synchronen Fehler abgeschlossen.")
return result
-- by Larsiopuw
