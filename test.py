import elegantt
chartsize = (720,320)
bgcolor = (255,255,255)
gchart = elegantt.EleGantt( chartsize, bgcolor, today="2019-10-15")
gchart.draw_calendar()
gchart.draw_campain("2019-10-15","2019-10-18","Hello")
gchart.draw_campain("2019-10-20","2019-10-23","Hello")
gchart.draw_campain("2019-10-24","2019-10-29","Hello")
gchart.save("test_basic_1.png")
