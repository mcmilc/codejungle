/*From Book: Algorithmic Thinking - Daniel Zingaro (Chapter 2)

 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NFLAKES 10000
#define MAX_FLAKE 10
#define SIZE 6

typedef struct snowflake_node
{
    int snowflake[SIZE];
    struct snowflake_node *next;
} snowflake_node;

void identify_identical_single(int values[]);
void identify_identical_double(int snowflakes[][6]);
int identical_right(int snow1[], int snow2[], int start);
int identical_left(int snow1[], int snow2[], int start);
int are_snowflakes_identical(int snow1[], int snow2[]);
int build_snowflake_dict(snowflake_node **snowflake_dict);
snowflake_node *generate_new_snowflake();
int code(int snowflake[]);

void identify_identical_single(int values[])
{
    int i, j;
    for (i = 0; i < SIZE; i++)
    {
        for (j = i + 1; j < SIZE; j++)
        {
            if (values[i] == values[j])
            {
                printf("Twin integer %d found at %d and %d\n", values[i], i, j);
                return;
            }
        }
    }
    printf("No twin integers in input found\n");
}

void identify_identical_double(int snowflakes[][SIZE])
{
    int i, j;
    for (int i = 0; i < SIZE; i++)
    {
        for (j = i + 1; j < SIZE; j++)
        {
            if (are_snowflakes_identical(snowflakes[i], snowflakes[j]))
            {
                printf("Twin snowflakes snow%d, snow%d found\n", i + 1, j + 1);
            }
        }
    }
}
/*
- n is length of snowflakes
*/
int identical_right(int snow1[], int snow2[], int start)
{
    int offset;
    for (offset = 0; offset < SIZE; offset++)
    {
        if (snow1[offset] != snow2[(start + offset) % SIZE])
            return 0;
    }
    return 1;
}

int identical_left(int snow1[], int snow2[], int start)
{
    int offset, snow2_index;
    for (offset = 0; offset < SIZE; offset++)
    {
        snow2_index = start - offset;
        if (snow2_index <= -1)
            snow2_index = snow2_index + SIZE;
        if (snow1[offset] != snow2[snow2_index])
            return 0;
    }
    return 1;
}

int are_snowflakes_identical(int snow1[], int snow2[])
{
    int start;
    for (start = 0; start < SIZE; start++)
    {
        if (identical_right(snow1, snow2, start))
            return 1;
        if (identical_left(snow1, snow2, start))
            return 1;
    }
    return 0;
}

void test_identify_single()
{
    int a[SIZE] = {1,
                   2,
                   3,
                   1,
                   5,
                   6};
    identify_identical_single(a);
}

int code(int snowflake[])
{
    int sum = 0;
    int i = 0;
    for (i = 0; i < SIZE; i++)
    {
        sum += snowflake[i];
    }
    sum = sum % NFLAKES;
    return sum;
}

void test_snowflakes_single_comparison()
{
    int snow1[6] = {1, 2, 3, 4, 5, 6};
    int snow2[6] = {4, 5, 6, 1, 2, 3};
    int snow3[6] = {3, 2, 1, 6, 5, 4};

    if (are_snowflakes_identical(snow1, snow2))
        printf("snow1 and snow2 are identical\n");
    else
        printf("snow1 and snow2 are not identical\n");
    if (are_snowflakes_identical(snow1, snow3))
        printf("snow1 and snow3 are identical\n");
    else
        printf("snow1 and snow3 are not identical\n");
}

void test_snowflakes_pairwise_comparison()
{
    int snowflakes[SIZE][SIZE] = {{1, 2, 3, 4, 5, 6},
                                  {4, 5, 6, 1, 2, 3},
                                  {5, 6, 1, 2, 3, 4},
                                  {5, 6, 1, 3, 2, 4},
                                  {3, 2, 1, 6, 5, 4},
                                  {3, 2, 1, 4, 5, 6}};
    identify_identical_double(snowflakes);
}

snowflake_node *generate_new_snowflake()
{
    snowflake_node *snode = (snowflake_node *)malloc(sizeof(snowflake_node));
    if (snode != NULL)
    {
        for (int i = 0; i < SIZE; i++)
        {
            snode->snowflake[i] = (rand() % MAX_FLAKE) + 1;
        }
        snode->next = NULL;
    }
    else
    {
        printf("Malloc error when creating new snowflake node (function generate_new_snowflake)\n");
        return NULL;
    }
    return snode;
}

int build_snowflake_dict(snowflake_node **snowflake_dict)
{
    if (snowflake_dict == NULL)
        return -1;
    for (int i = 0; i < NFLAKES; i++)
    {
        snowflake_dict[i] = NULL;
    }
    for (int i = 0; i < NFLAKES; i++)
    {
        snowflake_node *new_flake = generate_new_snowflake();
        if (new_flake == NULL)
        {
            printf("Error creating new_flake\n");
            return -1;
        }
        int snowflake_code = code(new_flake->snowflake);
        new_flake->next = snowflake_dict[snowflake_code];
        snowflake_dict[snowflake_code] = new_flake;
        // printf("Done creating flake %d with code %d\n", i, snowflake_code);
    }
    return 1;
}

void disp_snowflake(int snowflake[], char name[])
{
    printf("%s", name);
    for (int i = 0; i < SIZE; i++)
        printf("%d ", snowflake[i]);
    printf("\n");
}

void identify_identical_hash(snowflake_node *snowflakes[])
{
    snowflake_node *node1 = NULL;
    snowflake_node *node2 = NULL;
    for (int i = 0; i < NFLAKES; i++)
    {
        node1 = snowflakes[i];
        while (node1 != NULL)
        {
            node2 = node1->next;
            while (node2 != NULL)
            {
                if (are_snowflakes_identical(node1->snowflake, node2->snowflake))
                {
                    printf("Twin snowflakes found at code %d\n", i);
                    disp_snowflake(node1->snowflake, "snowflake 1: ");
                    disp_snowflake(node2->snowflake, "snowflake 2: ");
                }
                node2 = node2->next;
            }
            node1 = node1->next;
        }
    }
}

void free_snowflake_mem(snowflake_node **snowflake_dict)
{
    if (snowflake_dict != NULL)
    {
        int i;
        for (i = 0; i < NFLAKES; i++)
        {
            snowflake_node *current_node = snowflake_dict[i];
            snowflake_node *next = NULL;
            while (current_node != NULL)
            {
                next = current_node->next;
                free(current_node);
                current_node = next;
            }
        }
        free(snowflake_dict);
    }
}

int test_snowflake_comparison_hash()
{
    srand(time(NULL));
    int result;
    snowflake_node **snowflake_dict = (snowflake_node **)malloc(NFLAKES * sizeof(snowflake_node *));
    result = build_snowflake_dict(snowflake_dict);
    if (result == -1)
        return -1;
    if (snowflake_dict == NULL)
    {
        fprintf(stderr, "Malloc error when creating snowflake dictionary\n");
        free(snowflake_dict);
        return -1;
    }
    printf("Done building snowflakes\n");

    const char *text = "Flake";
    for (int i = 0; i < NFLAKES; i++)
    {
        snowflake_node *current_flake = snowflake_dict[i];
        while (current_flake != NULL)
        {
            int length = snprintf(NULL, 0, "%s %d", text, i) + 1; // +1 for the null terminator
            char *formattedString = (char *)malloc(length * sizeof(char));
            if (formattedString == NULL)
            {
                fprintf(stderr, "Memory allocation for flake name failed\n");
                free_snowflake_mem(snowflake_dict);
                return -1;
            }
            sprintf(formattedString, "%s %d\n", text, i);
            // disp_snowflake(current_flake->snowflake, formattedString);
            free(formattedString);
            current_flake = current_flake->next;
        }
    }
    identify_identical_hash(snowflake_dict);
    printf("Done with snowflake twin search\n");
    free_snowflake_mem(snowflake_dict);
}
int main()
{
    int result;
    result = test_snowflake_comparison_hash();
    if (result == -1)
        printf("Error\n");
    else
        printf("Success\n");
    return 0;
}