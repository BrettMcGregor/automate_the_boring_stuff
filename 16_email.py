import smtplib
smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
print(type(smtpObj))

smtpObj.ehlo()

smtpObj.starttls()

# changed security on the email account below to allow 'less secure apps'
smtpObj.login("burnerburner16@gmail.com", "H6jHf9NQuVQfm5a")

smtpObj.sendmail("burnerburner16@gmail.com", ["pepper.andrea@gmail.com", "brett.w.mcgregor@gmail.com"],
                 "Subject: So long.\n"
                 "Dear Someone,\n"
                 "Be nice to me or I might send you one hundred thousand spam email per day.\n"
                 "Sincerely, Hater.\n"
                 "P.S. Please do not reply to this email as I really hate spam.")

smtpObj.quit()
