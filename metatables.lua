local t = { 1, 2, 3 }

local mt = {

	__index = function(t, k)
		if k == "four" then
			return 5
		else
			return rawget(t, k)
		end
	end,
}
setmetatable(t, mt)

print(t[2]) --RETURN 2
print(t.four) --return 5
