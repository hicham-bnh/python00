# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mobenhab <mobenhab@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 17:27:30 by mobenhab          #+#    #+#              #
#    Updated: 2026/01/12 14:02:21 by mobenhab         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    day = 1
    last_day = int(input("Days until harvest: "))
    while day <= last_day:
        print("Day ", day)
        day+=1
    print("Harvest time!") 