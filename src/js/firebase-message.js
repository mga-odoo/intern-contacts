
$("#save_button").click(function () {
  $.ajax({
    url: "/signup/configure",
    type: 'POST',
    data: $('form').serialize(),
    success: function(response) {
      localStorage.setItem("profile_token", response.profile_token);
      $("#message-success").show();
      $("#profile_url").attr("href", response.url);
      console.log(response);
    },
    error: function(error) {
      console.log(error);
    },
  });
});

function setToken(currentToken) {
  localStorage.setItem("subscription_token", currentToken);
}

function sendToken(currentToken) {
  console.log(currentToken);
  $.ajax({
    url: "/profile/notification/enable",
    type: 'POST',
    data: {
      'currentToken':currentToken,
      'profile_edit': $("#profile_edit").val()
    },
    success: function(response) {
      console.log(response);
    },
    error: function(error) {
      console.log(error);
    }
  });
}

$( document ).ready(function() {
  var config = {
    apiKey: "AIzaSyDI0iuXejmB08RavaMa7KjJqQHFJhd4q-c",
    authDomain: "core-craft-233309.firebaseapp.com",
    databaseURL: "https://core-craft-233309.firebaseio.com",
    projectId: "core-craft-233309",
    storageBucket: "core-craft-233309.appspot.com",
    messagingSenderId: "51827162095",
  };
  firebase.initializeApp(config);

  const messaging = firebase.messaging();
  messaging.usePublicVapidKey('BL-hBhS5ddQpTivWGyDS7n_9ewxPyKAdL6vBPPaE4x29GJZiYVewgNv_oAFddqEeCXBSzZ5B_IFLfB_-F3EuRcI');

  messaging.onMessage(function(payload) {
    console.log('Message received. ', payload);
  });

  messaging.requestPermission().then(function() {
    messaging.onTokenRefresh(function() {
      messaging.getToken().then(function(refreshedToken) {
        console.log('Token refreshed.');
        setToken(false);
        sendToken(refreshedToken);
      }).catch(function(err) {
        console.log('Unable to retrieve refreshed token ', err);
        showToken('Unable to retrieve refreshed token ', err);
      });
    });
  }).catch(function(err) {
    console.log('Unable to get permission to notify.', err);
  });

  var profile_token = localStorage.getItem("profile_token");
  if(profile_token) {
    $("#notification_bar").show();
  }

});

$("#enable-notification").click(function () {
  const messaging = firebase.messaging();
  
  var subscription_token = localStorage.getItem("subscription_token");
  if(subscription_token) {
    new Notification ('Permission Granted', {
      'body': "You will start getting messages for an important messages"
    });
    return;
  }

  messaging.requestPermission().then(function() {
    messaging.getToken().then(function(currentToken) {
      if (currentToken) {
        setToken(currentToken);
        sendToken(currentToken);

        new Notification ('Permission Granted', {
          'body': "You will start getting messages for an important messages"
        });

      } else {
        console.log('No Instance ID token available. Request permission to generate one.');
      }
    }).catch(function(err) {
        console.log('An error occurred while retrieving token. ', err);
    });
  }).catch(function(err) {
    console.log('Unable to get permission to notify.', err);
  });
});