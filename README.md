# saltpay-pairprogramming-assignment
Pairing exercise

We need to further iterate on your solution to the take-home test for wishing people a happy birthday
New data format and location

We'd like for the data to be loaded from a CSV file from disk

It now has the person's email address.


 last_name, first_name, date_of_birth, email
 Doe, John,1982/10/08, john.doe@foobar.com
 Ann, Mary, 1975/09/11, mary.ann@foobar.com

Email the greeting

Rather than printing happy birthday, send an email to them. To send an email, use the API detailed below.

This is a pairing exercise so feel free to exchange ideas with us, ask questions and bounce ideas.

Good luck!
Shakey emailer

Shakey emailer will send emails for you, most of the time!


    POST $BASE_URL

    {"to":"chris.james@saltpay.co", "from": "amazing-candidate@hotmail.com", "subject":"Happy Birthday!", "body":"Wishing you a happy day" }

On success you'll receive a response with a HTTP status of 202 (accepted)

Sometimes sending email fails though....