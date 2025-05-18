from datetime import datetime
x=datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) ##-> prints Saturday as per time ##%B%C%D

print("#####strftime#####")
strftime_arguments={
    "%A":"WeekDayFull version",
    "%a":"WeekDayShort version",
    "%w":"Weekday as number 0-6 0 is sunday",
    "%d":"Day of month 01-31",
    "%b":"Month name short",
    "%B":"Month name full",
    "%m":"Month as number 1-12",
    "%y":"Year Short without century",
    "%Y":"Year full version",
    "%H":"Hour 00-24",
    "%I":"Hour 00-12",
    "%p":"AM/PM",
    "%M":"Minute",
    "%S":"Second",
    "%f":"micorseconds 0 - 999999",
    "%z":"UTC offset  +0100",
    "%Z":"Timezone CST",
    "%j":"Day in number 1-366",
    "%U":"Week number 0-53 Sunday as first week",
    "%W":"Week number 0-52 Monday as first week",
    "%c":"Local version of date and time Mon Dec 31 17:41:00 2018",
    "%C":"Century",
    "%x":"Local version of date",
    "%X":"local version of time",
    "%%":"a % character",
    "%G":"year ISO8061",
    "%u":"week day ISO8061",
    "%V":"weeknumber ISO8061",
    }
print(x.strftime("%j"))
for k,v in strftime_arguments.items():
    s=x.strftime(k)
    print(f"{k}  {v} ---->  {s}")


x=datetime(2024, 5 ,17, 7, 8, 30, 110111)  ###YYYY MM DD HH MM SS microseconds 0..999999
print(x)