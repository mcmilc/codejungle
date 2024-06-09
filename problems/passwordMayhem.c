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

int test_password_ver1(void);
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
int already_added(char all_substrings[][MAX_PASSWORD + 1], int total_substrings, char *password_in)
{
    for (int i = 0; i < total_substrings; i++)
        if (strcmp(all_substrings[i], password_in) == 0)
            return 1;
    return 0;
}
int test_substring_generation()
{
    char password[MAX_PASSWORD + 1];
    char substring[MAX_PASSWORD + 1];
    scanf("%s", password);
    int password_length = strlen(password);
    int n_to_copy;
    for (int i = 0; i < password_length; i++)
        for (int j = i; j < password_length; j++)
        {
            n_to_copy = j - i + 1;
            printf("N-to-copy: %d, i=%d, j=%d\n", n_to_copy, i, j);
            strncpy(substring, &password[i], n_to_copy);
            substring[n_to_copy] = '\0';
            printf("Substring: %s\n", substring);
        }
    return 1;
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
    return 1;
}
void free_node_mem(password_node **hash_table)
{
    int NCODES = 1 << NUM_BITS;
    if (hash_table != NULL)
    {
        int i;
        for (i = 0; i < NCODES; i++)
        {
            password_node *current_node = hash_table[i];
            password_node *next = NULL;
            while (current_node != NULL)
            {
                next = current_node->next;
                free(current_node);
                current_node = next;
            }
        }
        free(hash_table);
    }
}

int test_password_ver1(void)
{
    password_node **hash_table = (password_node **)malloc((1 << NUM_BITS) * sizeof(password_node *));
    if (hash_table == NULL)
    {
        fprintf(stderr, "Malloc error with hash table\n");
        exit(1);
    }
    printf("Hash_table declared\n");
    int num_ops, op, op_type, i, j;
    char password[MAX_PASSWORD + 1], substring[MAX_PASSWORD + 1];
    password_node *password_ptr;

    int total_substrings = MAX_PASSWORD * MAX_PASSWORD;
    scanf("%d", &num_ops);
    for (op = 0; op < num_ops; op++)
    {
        scanf("%d%s", &op_type, password);
        int pL = strlen(password);
        if (op_type == 1)
        {
            char all_substrings[total_substrings][MAX_PASSWORD + 1];
            for (int k = 0; k < total_substrings; k++)
                strcpy(all_substrings[k], "");
            int counter = 0;
            for (i = 0; i < pL; i++)
            {
                for (j = i; j < pL; j++)
                {
                    int num_copy = j - i + 1;
                    strncpy(substring, &password[i], num_copy);
                    substring[num_copy] = '\0';
                    if (already_added(all_substrings, total_substrings, substring) == 0)
                    {
                        strcpy(all_substrings[counter], substring);
                        printf("Adding substring: %s\n", substring);
                        add_to_hash_table(hash_table, substring);
                        counter++;
                    }
                }
            }
        }
        else
        {
            password_ptr = in_hash_table(hash_table, password);
            if (!password_ptr)
                printf("0\n");
            else
                printf("%d\n", password_ptr->total);
        }
    }
    free_node_mem(hash_table);
    return 0;
}

int main()
{
    // int success = test_oaat();
    // test_substring_generation();
    test_password_ver1();
    return 1;
}