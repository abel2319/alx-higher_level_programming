#include "lists.h"
/**
 * number_elts - count the number of elts in a list
 * @head: list where we count
 *
 * Return: the number of elts
 */
int number_elts(listint_t **head)
{
	int rtn = 0;
	listint_t *tmp = *head;

	while (tmp != NULL)
	{
		rtn++;
		tmp = tmp->next;
	}
	return (rtn);
}

/**
 * is_palidrome - verify if a list is a palindrome
 * @head: list
 *
 * Return: 1 if it is
 * 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int i = 0, nbr = 1, j = 0, t = 0;
	listint_t *tmp, *begin, *end;

	if (*head != NULL)
	{
		tmp = *head;
		begin = *head;
		end = *head;

		while (tmp->next != NULL)
		{
			nbr++;
			tmp = tmp->next;
		}

		while (i != (nbr / 2))
		{
			end = end->next;
			i++;
		}

		while (i != 0)
		{
			if (tmp->n != begin->n)
				return (0);
			else
			{
				begin = begin->next;
				tmp = end;
				t = (nbr % 2 == 0) ? i - 2 : i - 1;
				for(j = 0; j < t; j++)
					tmp = tmp->next;
			}
			i--;
		}
	}
	return (1);
}
