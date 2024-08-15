#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *parseLine(char *line) {
  int leftPointer = 0;
  int rightPointer = strlen(line) - 1;
  int foundL = 0;
  int foundR = 0;
  char *numbers = malloc(3 * sizeof(char));

  if (numbers == NULL) {
    printf("Memory allocation failed \n");
    return NULL;
  }

  numbers[0] = '0';
  numbers[1] = '0';
  numbers[2] = '\0';

  while (leftPointer < rightPointer || !foundL || !foundR) {
    if (!foundL && isdigit(line[leftPointer])) {
      numbers[0] = line[leftPointer];
      foundL = 1;
    }

    if (!foundR && isdigit(line[rightPointer])) {
      numbers[1] = line[rightPointer];
      foundR = 1;
    }

    leftPointer++;
    rightPointer--;
  }

  return numbers;
}

int parseInput(FILE *ptr) {
  int total = 0;
  char str[50];

  while (fgets(str, sizeof(str), ptr) != NULL) {
    char *parsedNumbers = parseLine(str);
    if (parsedNumbers != NULL) {
      total += atoi(parsedNumbers);
      free(parsedNumbers);
    }
  }

  return total;
}

int main() {
  FILE *ptr;

  ptr = fopen("./data.txt", "r");

  if (ptr == NULL) {
    printf("Error opening file.\n");
    return 1;
  }
  // parseInput(ptr);
  printf("Total: %d\n", parseInput(ptr));

  fclose(ptr);
}
