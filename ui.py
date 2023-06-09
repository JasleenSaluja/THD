import pygame

class UI:
    def __init__(self,surface):
        
        #setup
        self.display_surface = surface

        #coins collected
        self.coins_display=pygame.image.load('graphics/ui/0.png').convert_alpha()
        self.coin_display_rect=self.coins_display.get_rect(topleft=(45,45))
        self.font=pygame.font.SysFont('bruno ace',45)

    def show_coins(self,amount):
        self.display_surface.blit(self.coins_display,self.coin_display_rect)
        coin_amount_surf=self.font.render(str(amount),False,'white')
        coin_amount_rect=coin_amount_surf.get_rect(midleft=(self.coin_display_rect.right+6,self.coin_display_rect.centery +3))
        self.display_surface.blit(coin_amount_surf,coin_amount_rect)
        