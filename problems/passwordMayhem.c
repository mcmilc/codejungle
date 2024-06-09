#define hashsize(n) ((unsigned long)1 << (n))
#define hashmask(n) (hashsize(n) - 1)
#define MAX_PASSWORD 10
#define NUM_BITS 20
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct password_node
{
    char password[MAX_PASSWORD + 1];
    int total;
    struct password_node *next;
} password_node;

unsigned long
oaat(char *key, unsigned long len, unsigned long bits)
{
    unsigned long hash, i;
    for (hash = 0, i = 0; i < len; i++)
    {
        hash += key[i];
        hash += (hash << 10);
        hash ^= (hash >> 6);
    }
    hash += (hash << 3);
    hash ^= (hash >> 11);
    hash += (hash << 15);
    return hash & hashmask(bits);
}

password_node *in_hash_table(password_node *hash_table[], char *password_in)
{
    unsigned password_code;
    password_node *password_ptr;
    password_code = oaat(password_in, strlen(password_in), NUM_BITS);
    password_ptr = hash_table[password_code];
    while (password_ptr)
    {
        if (strcmp(password_ptr->password, password_in) == 0)
            return password_ptr;
        password_ptr = password_ptr->next;
    }
    return NULL;
}

void add_to_hash_table(password_node *hash_table[], char *password_in)
{
    unsigned password_code;
    password_node *password_ptr;

    password_ptr = in_hash_table(hash_table, password_in);
    if (!password_ptr)
    {
        // password not in hash-table yet
        password_code = oaat(password_in, strlen(password_in), NUM_BITS);
        password_ptr = malloc(sizeof(password_node));
        if (password_ptr == NULL)
        {
            fprintf(stderr, "Malloc error\n");
            exit(1);
        }
        strcpy(password_ptr->password, password_in);
        password_ptr->total = 0;
        password_ptr->next = hash_table[password_code];
        hash_table[password_code] = password_ptr;
    }
    // password in hash-table
    password_ptr->total++;
}

int test_oaat(void)
{
    char **passwords;
    int N_PASSWORDS = 6;
    unsigned *codes;
    passwords = (char **)malloc(N_PASSWORDS * sizeof(char *));
    codes = (unsigned *)malloc(N_PASSWORDS * sizeof(unsigned));

    passwords[0] = "radish";
    passwords[1] = "brandish";
    passwords[2] = "hsid";
    passwords[3] = "dish";
    passwords[4] = "shid";
    passwords[5] = "dish";

    for (int i = 0; i < N_PASSWORDS; i++)
    {
        codes[i] = oaat(passwords[i], strlen(passwords[i]), NUM_BITS);
        printf("Code [%d]: %u\n", i + 1, codes[i]);
    }
}

int main()
{
    test_oaat();
}