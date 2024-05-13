import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

String host = '192.168.15.156';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'To-Do List App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const LoginScreen(),
    );
  }
}

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  String? _errorMessage;

  Future<void> _login() async {
    var url = Uri.parse('http://$host:5000/token');
    try {
      var response = await http.post(
        url,
        headers: {'Content-Type': 'application/json; charset=UTF-8'},
        body: jsonEncode({
          'username': _usernameController.text,
          'password': _passwordController.text,
        }),
      );

      if (response.statusCode == 200) {
        var data = json.decode(response.body);
        Navigator.of(context).pushReplacement(
          MaterialPageRoute(builder: (_) => ToDoScreen(token: data['token'])),
        );
      } else {
        setState(() {
          _errorMessage = "Login failed: ${response.body}";
        });
      }
    } catch (e) {
      setState(() {
        _errorMessage = "Login failed: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            if (_errorMessage != null) Text(_errorMessage!, style: TextStyle(color: Colors.red, fontWeight: FontWeight.bold)),
            TextField(
              controller: _usernameController,
              decoration: InputDecoration(labelText: 'Username'),
            ),
            TextField(
              controller: _passwordController,
              obscureText: true,
              decoration: InputDecoration(labelText: 'Password'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _login,
              child: Text('Login'),
            ),
          ],
        ),
      ),
    );
  }
}

class ToDoScreen extends StatefulWidget {
  final String token;

  const ToDoScreen({Key? key, required this.token}) : super(key: key);

  @override
  _ToDoScreenState createState() => _ToDoScreenState();
}

class _ToDoScreenState extends State<ToDoScreen> {
  final TextEditingController _titleController = TextEditingController();
  final TextEditingController _descriptionController = TextEditingController();
  List tasks = []; // This should ideally be a list of a more specific type
  String _token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNTU2MDc5MiwianRpIjoiNjU2ZDFhNGItYzNhNi00MjQzLWJlYmEtZjMyNjdhNjhlMzU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MywibmJmIjoxNzE1NTYwNzkyLCJleHAiOjE3MTU1NjE2OTJ9.CGSS4Dad2Hm8m54BvPNb4YVVzR9-oHygCeq9YwVc8PE'; // Store JWT token

  @override
  void initState() {
    super.initState();
    _fetchTasks();
  }

  Future<void> _fetchTasks() async {
    var url = Uri.parse('http://$host:5000/tasks');  // Use your actual IP
    try {
      print(_token);  
      var response = await http.get(url, headers: {
        'Authorization': 'Bearer $_token'
      });

      print('Response status: ${response.statusCode}');
      print('Response body: ${response.body}');

      if (response.statusCode == 200) {
        var data = json.decode(response.body);
        setState(() {
          tasks = data is List ? data : data['tasks'];  // Adjust based on actual response
        });
      } else {
        print('Failed to fetch tasks. Server responded with: ${response.statusCode} ${response.body}');
      }
    } catch (e) {
      print('Failed to load tasks. Exception: $e');
    }
  }

  Future<void> _addTask() async {
    var url = Uri.parse('http://$host:5000/tasks');
    await http.post(
      url,
      headers: {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Bearer $_token',
      },
      body: jsonEncode({
        'title': _titleController.text,
        'description': _descriptionController.text,
      }),
    );
    _fetchTasks();
  }

  Future<void> _updateTask(dynamic task, bool isComplete) async {
    var url = Uri.parse('http://$host:5000/tasks/${task['id']}');
    await http.put(
      url,
      headers: {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Bearer $_token',
      },
      body: jsonEncode({
        'title': task['title'],
        'description': task['description'],
        'is_complete': isComplete,
      }),
    );
    _fetchTasks();
  }

  Future<void> _deleteTask(int taskId) async {
    var url = Uri.parse('http://$host:5000/tasks/$taskId');
    await http.delete(url, headers: {
      'Authorization': 'Bearer $_token',
    });
    _fetchTasks();
  }

  Future<void> _editTaskDialog(dynamic task) async {
    TextEditingController titleController = TextEditingController(text: task['title']);
    TextEditingController descriptionController = TextEditingController(text: task['description']);

    return showDialog<void>(
      context: context,
      barrierDismissible: false, // user must tap button!
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Edit Task'),
          content: SingleChildScrollView(
            child: ListBody(
              children: <Widget>[
                TextField(
                  controller: titleController,
                  decoration: const InputDecoration(labelText: 'Title'),
                ),
                TextField(
                  controller: descriptionController,
                  decoration: const InputDecoration(labelText: 'Description'),
                ),
              ],
            ),
          ),
          actions: <Widget>[
            TextButton(
              child: const Text('Cancel'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
            TextButton(
              child: const Text('Save'),
              onPressed: () {
                task['title'] = titleController.text;
                task['description'] = descriptionController.text;
                _updateTask(task, task['is_complete']);
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('To-Do List'),
      ),
      body: Column(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              controller: _titleController,
              decoration: const InputDecoration(labelText: 'Title'),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              controller: _descriptionController,
              decoration: const InputDecoration(labelText: 'Description'),
            ),
          ),
          ElevatedButton(
            onPressed: _addTask,
            child: const Text('Add Task'),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: tasks.length,
              itemBuilder: (context, index) {
                final task = tasks[index];
                return ListTile(
                  title: Text(task['title']),
                  subtitle: Text(task['description']),
                  onTap: () => _editTaskDialog(task),
                  trailing: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Checkbox(
                        value: task['is_complete'],
                        onChanged: (bool? value) {
                          print("Checkbox changed to: $value");
                          _updateTask(task, value ?? false);
                        },
                      ),
                    ],
                  ),
                  onLongPress: () {
                    _deleteTask(task['id']);
                  },
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}

