curl -X POST -H "Authorization: key=AAAADBEju-8:APA91bEcQryvsB2h4AZg4-bNYJoIGrx-YJd48ei5A4D4g6mQbgYjLQtHLdVtSnrtLBnCC7sp4HM5PSf-JingqgtizhQqLH32fCM_geqlPion0bn3xsfOp7K_LAYWvUorexunw2fSUJU2" -H "Content-Type: application/json" -d '{
  "notification": {
    "title": "Notification Title",
    "body": "Message body part, you can add up to 256 chars",
    "icon": "firebase-logo.png",
    "click_action": "http://localhost:8080/contacts"
  },
  "to": "fD9DiZpHpIQ:APA91bEntvaYLYlWCk4zoayzwFVEXw4YG9efVjED5iBCqV2t1yVZx87OI8SuqWmW6mhGW6DVIx2ZarjNxUlbWUfcyeRzuTh0kASdJDb4sxJmtp65H_YeiB3KyLSLXb5czVOdI0Q8QGSi"
}' "https://fcm.googleapis.com/fcm/send"
