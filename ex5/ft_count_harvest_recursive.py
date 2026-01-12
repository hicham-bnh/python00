# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mobenhab <mobenhab@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 16:34:00 by mobenhab          #+#    #+#              #
#    Updated: 2026/01/11 17:54:30 by mobenhab         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(day=1, last_day=None):
    if (last_day is None):
        last_day  = int(input("Days until harvest: "))
    if day <= last_day :
          print("Day ",day)
          return(ft_count_harvest_recursive(day + 1, last_day))
    else:
        print("Harvest time!")
        return 0