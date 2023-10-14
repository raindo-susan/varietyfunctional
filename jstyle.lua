local function riskyFunction(x)
	if x < 0 then
		error("negative value not allowed")
	else
		return math.sqrt(x)
	end
end

local function hookFunction(event)
	print("Hook triggered by event:" .. event)
end

--Setting the hook

debug.sethook(hookFunction, "c")

local status, result = pcall(riskyFunction, -1)

if status then
	print("Success! The result is " .. result)
else
	print("error occurred  because " .. result)
end

--injection

local function createGreeter(greeting)
	return function(name)
		print(greeting .. "," .. name .. "!")
	end
end

local greeter = createGreeter("hello")

greeter("World")
