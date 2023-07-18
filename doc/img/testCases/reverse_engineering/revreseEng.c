#include <stdio.h>
#include <string.h>

void secret_function()
{
    printf("Congratulations! You found the secret function!\n");
    printf("Here's your flag: CTF{Reverse_Engineering_Is_Fun}\n");
}

void check_password(const char *password)
{
    int valid = 0;
    char stored_password[] = "ofHur7s&M";

    if (strlen(password) == strlen(stored_password))
    {
        for (int i = 0; i < strlen(password); i++)
        {
            if (password[i] != stored_password[i])
            {
                valid = 0;
                break;
            }
            valid = 1;
        }
    }

    if (valid)
    {
        printf("Password accepted! Access granted.\n");
        secret_function();
    }
    else
    {
        printf("Invalid password! Access denied.\n");
    }
}

int main()
{
    char password[20];
    printf("Enter the password: ");
    scanf("%s", password);
    check_password(password);

    return 0;
}