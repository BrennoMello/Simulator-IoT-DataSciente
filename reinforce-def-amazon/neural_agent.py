
import torch.nn as nn



class NaiveAgent(nn.Module):

    def __init__(self):
        super(NaiveAgent,self).__init__()

        self.segmentation = self.create_segmentation_model()

    
    def create_segmentation_model(self):
        
        
        return ""