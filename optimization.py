from math import tanh
import openpyxl

total_weeks = 25
spanien = 17

weight_1 = 1
weight_2 = 1
weight_spanien = 5/7
weight_anfang = 10/7
weight_ende = 2

possible_weeks = [i for i in range(1, total_weeks+1)]
possible_weeks.remove(spanien)

def cost_function(woche_1, woche_2):
    variance_woche_1 = weight_anfang*tanh((woche_1)**2/25) + weight_2*tanh((abs(woche_1-woche_2)-1)**2/25) + weight_spanien*tanh((abs(spanien-woche_1)-1)**2/25) + weight_ende*tanh((max(possible_weeks)-woche_1)**2/25)
    variance_woche_2 = weight_anfang*tanh((woche_2)**2/25) + weight_1*tanh((abs(woche_2-woche_1)-1)**2/25) + weight_spanien*tanh((abs(spanien-woche_2)-1)**2/25) + weight_ende*tanh((max(possible_weeks)-woche_2)**2/25)

    cost_score = variance_woche_1+variance_woche_2

    return cost_score

weeks_1 = []
weeks_2 = []
scores = []
high_score = 0


wb = openpyxl.load_workbook("data.xlsx")
sheet = wb.active
row = 2


for w_1 in possible_weeks:
    for w_2 in possible_weeks:
        if w_1 == w_2:
            pass
        else:
            weeks_1.append(w_1)
            weeks_2.append(w_2)

            score = cost_function(w_1, w_2)
            scores.append(score)
            if score > high_score:
                high_score = score

            sheet[f"A{row}"] = w_1
            sheet[f"B{row}"] = w_2
            sheet[f"C{row}"] = score
            row += 1

wb.save("data.xlsx")