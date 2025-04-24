# iCal name day generator

-   Simple script that create .ics (alternatively .ical) file with 365 events for your calendar. Events are name days made of czech names. Replacing the .txt file with your own, you can use is as a template for you own language.

  ## What you might want to know

- As source for the list of names was used [wikipedia page](https://cs.wikipedia.org/wiki/Jmeniny). This table was converted using excel into .txt file. It is important to have this file in `UTF-16 LE` encoding due to some special characters in Czech.

- The output file did not include `VALARM` atribute for one very important reason. Google calendar doesn't want to accept notifications from files that wasn't created by google. I found that this problem is due to UID, that [needs to be known by Google calendar](https://support.google.com/calendar/thread/9627602/issue-google-calendar-ignores-alarms-notifications-in-events?hl=en) (it is impossible to generate one like this).
