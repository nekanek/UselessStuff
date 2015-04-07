Simple app which reminds to repeat learned stuff after 1, 7, 30 and 181 days.
Console so far.


### Add something you learned

    python add.py <-y> <-p days> "Learned piece description" <any optional tags>
    e.g.
    python add.py "Learned today piece" web js py cs
    python add.py -y "Learned yesterday" hh java
    python add.py -p 3 "Smth learned 3 days ago without tags"

### Check what to repeat today

    python today.py


### Check what to repeat some other day

    python agenda.py <shift in days> (0 by default)
    e.g. to get reminder for yesterday:
    python agenda.py -1
    e.g. to get reminder for the day after tomorrow:
    python agenda.py 2
