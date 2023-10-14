math.randomseed(os.time())

local a = math.random(1, 10)

local toro = function(a)
	while a < 12 do
		print("hello")
		a = a + 1
	end
end

pcall(toro, a)
