-- ISB Menu 2.2: place this Script in ServerScriptService in your own experience.
local Players=game:GetService("Players")
local Storage=game:GetService("ReplicatedStorage")
local Run=game:GetService("RunService")
local OWNER_NAMES={"Larsiopuw"}
local ADMIN_IDS={} -- Roblox UserIds, assigned by the owner.
local owners={}
for _,name in ipairs(OWNER_NAMES) do
    local ok,id=pcall(function() return Players:GetUserIdFromNameAsync(name) end)
    if ok then owners[id]=true else warn("ISB: Owner lookup failed for "..name) end
end
local bridge=Storage:FindFirstChild("ISBPresence")
if bridge then error("ISBPresence already exists. Install only one server script.") end
bridge=Instance.new("Folder"); bridge.Name="ISBPresence"; bridge.Parent=Storage
local request=Instance.new("RemoteFunction"); request.Name="Request"; request.Parent=bridge
local changed=Instance.new("RemoteEvent"); changed.Name="Changed"; changed.Parent=bridge
local members,lastRequest={},{}
local overhead=true
local function role(player)
    if owners[player.UserId] then return "Owner" end
    if table.find(ADMIN_IDS,player.UserId) then return "Admin" end
    return "Member"
end
local function snapshot()
    local users={}
    for player in pairs(members) do
        if player.Parent==Players then table.insert(users,{userId=player.UserId,role=role(player)}) end
    end
    return {protocol=1,overhead=overhead,users=users}
end
local function broadcast() changed:FireAllClients(snapshot()) end
request.OnServerInvoke=function(player,action,value)
    if type(action)~="string" or not ({register=true,leave=true,overhead=true,teleport=true})[action] then return {ok=false} end
    local now=os.clock()
    local limits=lastRequest[player] or {}; lastRequest[player]=limits
    if now-(limits[action] or -100)<(action=="register" and 1 or .4) then return {ok=false} end
    limits[action]=now
    if action=="register" then
        local first=members[player]==nil; members[player]=now
        if first then broadcast() end
        return snapshot()
    elseif action=="leave" then members[player]=nil; broadcast(); return {ok=true} end
    if not members[player] then return {ok=false} end
    if action=="overhead" then
        if role(player)=="Member" or type(value)~="boolean" then return {ok=false} end
        overhead=value; broadcast(); return snapshot()
    elseif action=="teleport" then
        if type(value)~="number" or value~=value then return {ok=false} end
        local target=Players:GetPlayerByUserId(value)
        local ownCharacter,targetCharacter=player.Character,target and target.Character
        local ownRoot=ownCharacter and ownCharacter:FindFirstChild("HumanoidRootPart")
        local targetRoot=targetCharacter and targetCharacter:FindFirstChild("HumanoidRootPart")
        local ownHumanoid=ownCharacter and ownCharacter:FindFirstChildOfClass("Humanoid")
        local targetHumanoid=targetCharacter and targetCharacter:FindFirstChildOfClass("Humanoid")
        if not target or target==player or not members[target] or not ownRoot or not targetRoot or not ownHumanoid or not targetHumanoid or ownHumanoid.Health<=0 or targetHumanoid.Health<=0 then return {ok=false} end
        ownCharacter:PivotTo(targetRoot.CFrame*CFrame.new(3,0,0))
        return {ok=true}
    end
    return {ok=false}
end
Players.PlayerRemoving:Connect(function(player) members[player]=nil; lastRequest[player]=nil; broadcast() end)
local elapsed=0
Run.Heartbeat:Connect(function(dt)
    elapsed=elapsed+dt
    if elapsed<10 then return end
    elapsed=0; local now=os.clock(); local dirty=false
    for player,lastSeen in pairs(members) do
        if player.Parent~=Players or now-lastSeen>65 then members[player]=nil; dirty=true end
    end
    if dirty then broadcast() end
end)
-- by Larsiopuw
