curl -X POST -H "Authorization: key=AAAADBEju-8:APA91bEcQryvsB2h4AZg4-bNYJoIGrx-YJd48ei5A4D4g6mQbgYjLQtHLdVtSnrtLBnCC7sp4HM5PSf-JingqgtizhQqLH32fCM_geqlPion0bn3xsfOp7K_LAYWvUorexunw2fSUJU2" -H "Content-Type: application/json" -d '{
  "notification": {
    "title": "Portugal vs. Denmark",
    "body": "5 to 1",
    "icon": "firebase-logo.png",
    "click_action": "http://localhost:8080/contacts"
  },
  "to": "c6SP1FgCJVI:APA91bGIW59-ShHL9PsKVO6_p8P6UeQqUbAc_tUG1jLE6Le_39sPLyRcKCy3PaSipbB8g8bPQTFEO2Gu7pQ8PRfTanNFR0YGzVqYzzWlGJnyhqoNH-p75ArT5VOamyQo13Pgawq51LFJ"
}' "https://fcm.googleapis.com/fcm/send"