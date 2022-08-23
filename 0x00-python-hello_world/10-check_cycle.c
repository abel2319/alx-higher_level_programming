#include "lists.h"
/**
 * check_cycle - Verify if a list is a cycle or not
 * @list: list where we verify
 *
 * Return: 1 if is a cycle
 * 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = NULL;
	listint_t *head =NULL;

	if(list != NULL)
	{
		head = list;
		tmp = list->next;
		while (tmp != NULL)
		{
			if (tmp == head)
			{
				return (1);
			}
			tmp = tmp->next;
		}
	}
	return (0);
}
