import 'package:flutter/foundation.dart';
import '../models/chat_message.dart';
import '../services/chat_service.dart';

class ChatProvider extends ChangeNotifier {
  List<ChatMessage> _messages = [];
  bool _isLoading = false;
  String _error = '';
  
  List<ChatMessage> get messages => _messages;
  bool get isLoading => _isLoading;
  String get error => _error;
  
  // Add message to list
  void addMessage(ChatMessage message) {
    _messages.add(message);
    notifyListeners();
  }
  
  // Send message
  Future<void> sendMessage(String text) async {
    if (text.trim().isEmpty) return;
    
    // Add user message
    final userMessage = ChatMessage(
      text: text,
      isUser: true,
      timestamp: DateTime.now(),
    );
    addMessage(userMessage);
    
    // Set loading state
    _isLoading = true;
    _error = '';
    notifyListeners();
    
    try {
      // Send to API
      final response = await ChatService.sendMessage(text);
      
      // Add bot reply
      final botMessage = ChatMessage(
        text: response['reply'] ?? 'Sorry, I cannot understand your question.',
        isUser: false,
        timestamp: DateTime.now(),
      );
      addMessage(botMessage);
      
    } catch (e) {
      _error = e.toString();
      // Add error message
      final errorMessage = ChatMessage(
        text: 'Sorry, there was an error connecting to the server. Please check your network connection or try again later.',
        isUser: false,
        timestamp: DateTime.now(),
      );
      addMessage(errorMessage);
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
  
  // Clear chat history
  Future<void> clearHistory() async {
    try {
      await ChatService.clearHistory();
      _messages.clear();
      _error = '';
      notifyListeners();
    } catch (e) {
      _error = e.toString();
      notifyListeners();
    }
  }
  
  // Check server status
  Future<bool> checkServerHealth() async {
    return await ChatService.checkHealth();
  }
}
