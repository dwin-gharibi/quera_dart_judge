import 'dart:io';

void main() {
    String? input1 = stdin.readLineSync();
    String? input2 = stdin.readLineSync();

    int num1 = int.parse(input1);
    int num2 = int.parse(input2);
    int sum = num1 + num2;
    print("$sum");
}
