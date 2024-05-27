// local_notifications.dart
// Construção de uma tela que permite realizar agendamentos de tempo para notificações locais.

import 'package:awesome_notifications/awesome_notifications.dart';
import 'package:flutter/material.dart';

class LocalNotifications extends StatefulWidget {
  const LocalNotifications({super.key});

  @override
  State<LocalNotifications> createState() => _LocalNotificationsState();
}

class _LocalNotificationsState extends State<LocalNotifications> {
  final TextEditingController _timeController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[400],
      appBar: AppBar(
        title: const Text('Agendamento de Notificações'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              "Agendamento de Notificações",
              style: TextStyle(color: Colors.white, fontSize: 24),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                keyboardType: TextInputType.number,
                controller: _timeController,
                decoration: const InputDecoration(
                  hintText: 'Digite o tempo em segundos',
                ),
              ),
            ),
            IconButton(
              onPressed: () {
                AwesomeNotifications()
                    .isNotificationAllowed()
                    .then((isAllowed) {
                  if (!isAllowed) {
                    AwesomeNotifications()
                        .requestPermissionToSendNotifications();
                  } else {
                    AwesomeNotifications().createNotification(
                        content: NotificationContent(
                      id: 1,
                      channelKey: 'test_channel',
                      color: Colors.blue,
                      title: "Hello, this is Jean Rothstein",
                      body: "Pascoli me ama",
                      criticalAlert: true,
                      wakeUpScreen: true,
                      payload: {'data': 'Jupiter exemplos'},
                    ));
                    // AwesomeNotifications().setListeners(
                    //   onActionReceivedMethod: (receivedNotification) {
                    //     if (receivedNotification.payload != null) {
                    //       print(
                    //           "Notification payload: ${receivedNotification.payload}");
                    //     }
                    //   },
                    // );
                  }
                });
              },
              icon: ClipRRect(  
                borderRadius: BorderRadius.circular(20.0),
                child: Image.asset(
                  'assets/tomato.png',
                  width: 100,
                  height: 100,
                  fit: BoxFit.contain,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
