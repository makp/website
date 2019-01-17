(* ::Package:: *)

Begin["makeSchedule`"]


listAllSimple[first_, last_, weekDays_]:=
(listDays = DayRange[first, last, #]&/@weekDays//Flatten//Sort;
DateString[#,{"Month", "-", "Day","-", "YearShort"}]&/@listDays)


(*listAll[first_, last_, weekDays_]:= 
(listDays = DayRange[first, last, #]&/@weekDays//Flatten//Sort;
listDaysByWeek = SplitBy[listDays,DateString[#,{"Week"}]&];
funcFormatting[list_]:= DateString[#,{"Month", "-", "Day"}]&/@list;
listWeeks = StringJoin["Week ",#]&/@ToString/@Range[Length@listDaysByWeek];
listFinal = Transpose[{listWeeks,funcFormatting/@listDaysByWeek}];
Print@listFinal)
(*TODO: Use "Apply[f,listDaysByWeek,{2}] for formatting the list*)*)


(* ::Text:: *)
(*The following export function produces an org-file:*)


(*exportFileOld[listRaw_]:=
(addSymbol[list_, sym_]:= StringJoin["\n\n",sym, " ",  # ]&/@list;
out1 =(addSymbol[{#[[1]]},"**"]<>addSymbol[#[[2]],"***"])&/@listRaw;
out2 = Append[out1, "\n \n** Final Exam\n"];
Export["schedule.org",out2,"List"])*)


fileNameToExport[lst_]:=
(firstMonth = DateString[lst[[1]],{"Month"}];
year = DateString[lst[[1]],{"Year"}];
term = <|"08" -> "Fall", "01" -> "Spring", "02" -> "Spring"|>[firstMonth];
"teachingDates" <> term <> year <> ".csv")


exportFile[listRaw_]:=
(Export[fileNameToExport@listRaw,listRaw,"Table", "LineSeparators" -> ", "])


End[]
