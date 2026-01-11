# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mobenhab <mobenhab@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 16:14:05 by mobenhab          #+#    #+#              #
#    Updated: 2026/01/11 16:19:02 by mobenhab         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
    length = input("Enter length: ")
    length = int(length)
    width = input("Enter width: ")
    width = int(width)
    print("Ploa area: ", length * width)