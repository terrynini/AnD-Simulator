#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char name[40] = "TBD";
char team[30] = "TBD";
char teammate[10][40];

void menu()
{
    puts("==================================");
    puts("|       BABY AnD SIMULATOR       |");
    puts("==================================");
    puts("| 1. CTF player profile          |");
    puts("| 2. Set  name                   |");
    puts("| 3. Join team                   |");
    puts("| 4. Add teammate                |");
    puts("| 5. Change teammate             |");
    puts("| 6. Exit                        |");
    puts("==================================");
    printf("> "); 
}

void listTeammate()
{
    for(int i = 0 ; i < 10 ; i++)
    {   
        printf("    %d. ", i+1);
        if(teammate[i][0] != 0)
            printf("%s", teammate[i]);
        puts("");
    }
}

void profile()
{
    printf("Name: %s\n", name);
    printf("Team: %s\n", team);    
    puts("Teammate:");
    listTeammate();
}

void sub_804858z()
{
    system("cat /home/simulator/flag");
}

void print(char* st)
{
    printf("%s", st);
    if(!strcmp(team,"T1Z334ckd00r="))
        sub_804858z();
}

void setName()
{
    char opt;
    char temp[31];

    printf("Input your name: ");
    read(STDIN_FILENO, temp, 40);
    temp[strcspn(temp, "\n")] = 0;
    printf("Is this your name ? %s [y/n] ", temp);
    scanf(" %c", &opt);
    getchar();
    if( opt == 'y' )
        strcpy(name, temp);
    else
        printf("Canceled\n");
}

void setTeam()
{
    char opt;
    char temp[31];

    printf("Your team name: ");
    read(STDIN_FILENO, temp, 30);
    temp[strcspn(temp, "\n")] = 0;
    printf("Is this your team? %s [y/n] ", temp);
    scanf(" %c", &opt);
    getchar();
    if( opt == 'y')
        strcpy(team,temp);
    else
        print("Canceled\n");
}
void addTeammate()
{
    char temp[31];
    listTeammate();
    printf("New member : ");
    read(STDIN_FILENO, temp, 30);
    temp[strcspn(temp, "\n")] = 0;
    for(int i = 0 ; i < 10 ; i++)
    {
        if(teammate[i][0] == 0)
        {
            strcpy(teammate[i], temp);
            return;
        }
    }
    printf("You already have 10 teammates\n");
} 

void chTeammate()
{
    int option;
    char temp[40];
    listTeammate();
    puts("Which member you want to change?");
    scanf(" %d", &option);
    if (option > 10)
    {
        puts("Out of range");
        return;
    }
    printf("New member : ");
    read(STDIN_FILENO, temp, 30);
    temp[strcspn(temp, "\n")] = 0;
    strcpy(teammate[option-1], temp);
}

int main()
{
    char buf[5];
    int choice;

    setbuf(stdin, 0);
    setbuf(stdout, 0);
    memset(teammate, 0, 400);
    while (1)
    {
        menu();
        read(STDIN_FILENO, buf,4);
        choice = atoi(buf);
        if(choice == 1)
            profile();
        else if(choice == 2)
            setName();
        else if(choice == 3)
            setTeam();
        else if(choice == 4)
            addTeammate();
        else if(choice == 5)
            chTeammate(); 
        else if(choice == 6)
            exit(0);
    }
    return 0;
}
