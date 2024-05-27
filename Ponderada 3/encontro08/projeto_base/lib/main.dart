import 'package:flutter/material.dart';
import 'package:awesome_notifications/awesome_notifications.dart';
import 'views/home.dart';
import 'views/local_notifications.dart';
import 'views/remove_background.dart';
import 'views/login_screen.dart';
import 'views/register_screen.dart';

void main() {
  AwesomeNotifications().initialize(null, [
    NotificationChannel(
        ledColor: Colors.blue,
        enableVibration: true,
        channelKey: "test_channel",
        channelName: "Test Notification",
        channelDescription: 'Basic Notification for the user')
  ]);
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Encontro 08',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      initialRoute: '/login',
      routes: {
        '/home': (context) => const Home(),
        '/local_notifications': (context) => const LocalNotifications(),
        '/remove_background': (context) =>
            const RemoveBackground(title: 'Remove Background'),
        '/login': (context) => LoginScreen(),
        '/register': (context) => RegisterScreen(),
      },
    );
  }
}
