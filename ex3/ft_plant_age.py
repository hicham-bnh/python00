# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mobenhab <mobenhab@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 16:25:33 by mobenhab          #+#    #+#              #
#    Updated: 2026/01/11 16:28:33 by mobenhab         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    age = input("Enter plant age in days: ")
    age = int(age)
    if (age > 60):
        print("Plant is ready to harvest!")
    else :
        print("Plant needs more time to grow.")