import elegantt

chartsize = (720,320)
bgcolor = (255,255,255)

gchart = elegantt.EleGantt( chartsize, bgcolor, today="2019-10-15")
gchart.set_font("ipaexg.ttf")
gchart.draw_calendar()
gchart.draw_campain("2019-10-15","2019-10-18","こんにちは")
gchart.draw_campain("2019-10-20","2019-10-23","こんにちは")
gchart.draw_campain("2019-10-24","2019-10-29","こんにちは")
gchart.save("test.png")
