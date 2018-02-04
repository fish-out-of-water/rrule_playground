def testGetDay():
	assert "MO" == getDayRaw(1, 1, 2018)
	assert "TU" == getDayRaw(2, 1, 2018)
	assert "WE" == getDayRaw(3, 1, 2018)
	assert "TH" == getDayRaw(4, 1, 2018)
	assert "FR" == getDayRaw(5, 1, 2018)
	assert "SA" == getDayRaw(6, 1, 2018)
	assert "SU" == getDayRaw(7, 1, 2018)

	assert "MO" == getDayRaw(8, 1, 2018)
	assert "TU" == getDayRaw(9, 1, 2018)

	assert "TH" == getDayRaw(1, 2, 2018)
	assert "FR" == getDayRaw(2, 2, 2018)
	assert "SA" == getDayRaw(3, 2, 2018)
	assert "SU" == getDayRaw(4, 2, 2018)
	assert "MO" == getDayRaw(5, 2, 2018)

	assert "SU" == getDayRaw(31, 12, 2017)
	assert "SA" == getDayRaw(30, 12, 2017)
	assert "FR" == getDayRaw(29, 12, 2017)
	assert "TH" == getDayRaw(28, 12, 2017)

	assert "WE" == getDayRaw(12, 4, 2017)
	assert "FR" == getDayRaw(24, 2, 2017)

	assert "TU" == getDayRaw(15, 11, 2016)
	assert "TU" == getDayRaw(29, 3, 2016)

testGetDay()