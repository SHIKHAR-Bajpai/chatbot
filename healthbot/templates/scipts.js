function sendMessage() {
    var userInput = document.getElementById('inputField').value;
    var chatbox = document.getElementById('chat');

    // Append user message to the chatbox
    chatbox.innerHTML += '<p style="color: #FFFFFF; padding: 0 10%; border-radius: 5px;">You: ' + userInput + '</p>';

    fetch('/api?query=' + userInput)
      .then(response => response.json())
      .then(data => {
        // Use the API response as botResponse
        var botResponse = data.output;
        chatbox.innerHTML += '<p style="color: #2ecc71">Bot: ' + botResponse + '</p>';
    
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });

    // Clear the input field
    document.getElementById('inputField').value = '';
  }


document.getElementById("inputField").addEventListener("keypress", function(event) {
    if (event.key === "Enter" && this.value.trim() !== "") {
      event.preventDefault();
      document.getElementById("submitButton").click();
    }
  });