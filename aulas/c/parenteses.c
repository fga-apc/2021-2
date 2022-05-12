#include <stdio.h>

int balanceado(char *text)
{
    int count = 0;
    for (int i = 0; text[i] != 0; i++)
    {
        if (text[i] == '(')
        {
            count++;
        }
        else if (text[i] == ')')
        {
            count--;
        }
        if (count < 0)
        {
            return 0;
        }
    }
    return (count == 0);
}

int main()
{
    char line[1001];

    while (1)
    {
        fgets(line, 1000, stdin); // lê uma linha
        if (line[0] == 0)
        {
            break;
        }
        if (balanceado(line))
        {
            printf("correct\n");
        }
        else
        {
            printf("incorrect\n");
        }
    }
    return 0;
}