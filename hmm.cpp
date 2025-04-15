#include <iostream>
#include <cstring>

void copyInput(char* dest, const char* src, size_t maxLen) {
    // Intended to prevent overflow, but the logic is flawed
    for (size_t i = 0; i <= maxLen; ++i) {
        dest[i] = src[i];
        if (src[i] == '\0') break;
    }
}

void processUserInput(const char* userInput) {
    char buffer[32];  // Fixed small buffer
    std::cout << "Processing input...\n";
    
    // Subtle bug: using strlen(userInput) as maxLen can exceed buffer size
    copyInput(buffer, userInput, strlen(userInput));

    std::cout << "Input received: " << buffer << "\n";
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <input>\n";
        return 1;
    }

    processUserInput(argv[1]);
    return 0;
}
