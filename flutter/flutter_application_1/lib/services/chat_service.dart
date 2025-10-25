import 'dart:convert';
import 'package:http/http.dart' as http;

class ChatService {
  static const String baseUrl = 'http://localhost:5000';
  
  // 发送消息到聊天机器人
  static Future<Map<String, dynamic>> sendMessage(String message, {String userId = 'default'}) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/chat'),
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode({
          'message': message,
          'user_id': userId,
        }),
      );
      
      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      } else {
        throw Exception('Server error: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Network error: $e');
    }
  }
  
  // Check server health status
  static Future<bool> checkHealth() async {
    try {
      final response = await http.get(Uri.parse('$baseUrl/health'));
      return response.statusCode == 200;
    } catch (e) {
      return false;
    }
  }
  
  // Clear chat history
  static Future<void> clearHistory({String userId = 'default'}) async {
    try {
      await http.post(
        Uri.parse('$baseUrl/clear_history'),
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode({
          'user_id': userId,
        }),
      );
    } catch (e) {
      throw Exception('Failed to clear history: $e');
    }
  }
}
