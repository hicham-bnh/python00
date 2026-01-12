# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mobenhab <mobenhab@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 16:53:49 by mobenhab          #+#    #+#              #
#    Updated: 2026/01/12 14:04:05 by mobenhab         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(first, second, therd):
    if (therd == "packets"):
        print(f"{first} seeds: {second} {therd} avaible")
    elif (therd == "grams"):
        print(f"{first} seeds: {second} {therd} avaible") 
    elif (therd == "area"):
        print(f"{first} seeds: covers {second} meters")
    else :
        print("Unknown unit type")
        