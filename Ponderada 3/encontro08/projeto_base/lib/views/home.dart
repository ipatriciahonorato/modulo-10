// home.dart
import 'package:flutter/material.dart';
import '../services/auth_service.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final AuthService _authService = AuthService();

  @override
  void initState() {
    super.initState();
    _checkAuth();
  }

  void _checkAuth() async {
    String? token = await _authService.getToken();
    if (token == null) {
      Navigator.pushReplacementNamed(context, '/login');
    }
  }

  void _logout() async {
    await _authService.logout();
    Navigator.pushReplacementNamed(context, '/login');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[400],
      appBar: AppBar(
        title: const Text('Seletor de Funcionalidades'),
        actions: [
          IconButton(
            icon: Icon(Icons.logout),
            onPressed: _logout,
          ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              "Agendamento de Notificações",
              style: TextStyle(color: Colors.white, fontSize: 24),
            ),
            IconButton(
              onPressed: () {
                // Navegar para a tela de agendamento de notificações locais
                Navigator.pushNamed(context, '/local_notifications');
              },
              icon: ClipRRect(
                borderRadius: BorderRadius.circular(20.0),
                child: Image.asset(
                  'assets/tomato.png',
                  width: 200,
                  height: 200,
                  fit: BoxFit.contain,
                ),
              ),
            ),
            const SizedBox(height: 20),
            const Text(
              "Remover de Fundo de Imagens",
              style: TextStyle(color: Colors.white, fontSize: 24),
            ),
            IconButton(
              onPressed: () {
                // Navegar para a tela de remoção de fundo de imagens
                Navigator.pushNamed(context, '/remove_background');
              },
              icon: ClipRRect(
                borderRadius: BorderRadius.circular(20.0),
                child: Image.asset(
                  'assets/shiba01.png',
                  width: 200,
                  height: 200,
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
