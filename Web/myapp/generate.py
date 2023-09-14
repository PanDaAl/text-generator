import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from django.contrib.staticfiles.storage import staticfiles_storage


SEQ_LEN = 128
BATCH_SIZE = 16
char_to_idx = {' ': 0, 'о': 1, 'е': 2, 'а': 3, 'и': 4, 'н': 5, 'т': 6, 'с': 7, 'л': 8, 'р': 9, 'в': 10,
               'к': 11, 'м': 12, 'д': 13, 'у': 14, ',': 15, 'п': 16, 'я': 17, 'ь': 18, 'ы': 19, 'г': 20,
               'б': 21, 'з': 22, 'ч': 23, '.': 24, 'й': 25, 'ж': 26, 'х': 27, 'ш': 28, '\n': 29, 'ю': 30,
               'ц': 31, 'щ': 32, 'э': 33, 'Н': 34, '!': 35, '-': 36, 'В': 37, '?': 38, 'П': 39, '—': 40,
               'С': 41, '…': 42, 'О': 43, 'К': 44, 'А': 45, 'М': 46, 'ф': 47, ':': 48, 'И': 49, 'Т': 50,
               'Д': 51, '"': 52, '«': 53, '»': 54, 'Я': 55, 'Б': 56, 'Г': 57, 'Л': 58, 'Ч': 59, 'З': 60,
               'ё': 61, 'Р': 62, 'Э': 63, 'Е': 64, 'У': 65, 'Х': 66, 'Ф': 67, 'ъ': 68, 'e': 69, 'Ш': 70,
               '1': 71, 'Ж': 72, 'a': 73, 'i': 74, 's': 75, 'n': 76, '2': 77, '0': 78, 'I': 79, 'o': 80,
               'r': 81, 't': 82, '9': 83, 'u': 84, '3': 85, 'm': 86, 'l': 87, 'Ц': 88, '4': 89, 'Ю': 90,
               '5': 91, '8': 92, '7': 93, 'c': 94, 'd': 95, '6': 96, 'X': 97, 'p': 98, 'V': 99, 'h': 100,
               'v': 101, 'Щ': 102, 'g': 103, 'b': 104, 'f': 105, 'é': 106, 'M': 107, 'q': 108, 'Й': 109, 'z': 110,
               'S': 111, 'A': 112, 'N': 113, 'j': 114, 'C': 115, 'L': 116, 'B': 117, 'y': 118, 'x': 119, 'P': 120,
               'E': 121, 'D': 122, 'è': 123, 'J': 124, 'w': 125, 'k': 126, 'R': 127, 'à': 128, 'H': 129, 'O': 130,
               'G': 131, 'T': 132, '_': 133, 'Ь': 134, 'ê': 135, 'F': 136, 'K': 137, 'Q': 138, 'Ы': 139, 'W': 140,
               'і': 141, 'U': 142, 'Z': 143, 'ô': 144, 'ç': 145, 'â': 146, 'ó': 147, 'î': 148, 'ü': 149, 'Ё': 150,
               'ѣ': 151, 'º': 152, '½': 153, 'Y': 154, 'ä': 155, 'ù': 156, 'ö': 157, 'œ': 158, 'á': 159, 'û': 160,
               '¼': 161, 'є': 162, 'Ъ': 163, 'ï': 164, 'ë': 165, 'ė': 166, 'Ç': 167, 'ß': 168, 'ò': 169, 'ї': 170,
               'ę': 171, 'ў': 172, 'ć': 173, 'ą': 174, 'Š': 175, 'š': 176, 'À': 177, 'ο': 178, 'ś': 179, 'α': 180,
               'β': 181, 'ý': 182, 'ј': 183, '場': 184, '工': 185, '罵': 186, '垢': 187, '馬': 188, '嘔': 189, '婆': 190,
               '駆': 191, 'Ü': 192, 'ό': 193, 'ν': 194, 'Ś': 195, 'ż': 196, 'å': 197, 'Ö': 198, 'ł': 199, '⅓': 200,
               'ѕ': 201, 'Ž': 202, 'ž': 203, 'τ': 204, 'í': 205, 'ň': 206, 'Ѕ': 207, 'č': 208, '¾': 209, 'ø': 210,
               'ґ': 211}
idx_to_char = {0: ' ', 1: 'о', 2: 'е', 3: 'а', 4: 'и', 5: 'н', 6: 'т', 7: 'с', 8: 'л', 9: 'р', 10: 'в',
               11: 'к', 12: 'м', 13: 'д', 14: 'у', 15: ',', 16: 'п', 17: 'я', 18: 'ь', 19: 'ы', 20: 'г',
               21: 'б', 22: 'з', 23: 'ч', 24: '.', 25: 'й', 26: 'ж', 27: 'х', 28: 'ш', 29: '\n', 30: 'ю',
               31: 'ц', 32: 'щ', 33: 'э', 34: 'Н', 35: '!', 36: '-', 37: 'В', 38: '?', 39: 'П', 40: '—',
               41: 'С', 42: '…', 43: 'О', 44: 'К', 45: 'А', 46: 'М', 47: 'ф', 48: ':', 49: 'И', 50: 'Т',
               51: 'Д', 52: '"', 53: '«', 54: '»', 55: 'Я', 56: 'Б', 57: 'Г', 58: 'Л', 59: 'Ч', 60: 'З',
               61: 'ё', 62: 'Р', 63: 'Э', 64: 'Е', 65: 'У', 66: 'Х', 67: 'Ф', 68: 'ъ', 69: 'e', 70: 'Ш',
               71: '1', 72: 'Ж', 73: 'a', 74: 'i', 75: 's', 76: 'n', 77: '2', 78: '0', 79: 'I', 80: 'o',
               81: 'r', 82: 't', 83: '9', 84: 'u', 85: '3', 86: 'm', 87: 'l', 88: 'Ц', 89: '4', 90: 'Ю',
               91: '5', 92: '8', 93: '7', 94: 'c', 95: 'd', 96: '6', 97: 'X', 98: 'p', 99: 'V', 100: 'h',
               101: 'v', 102: 'Щ', 103: 'g', 104: 'b', 105: 'f', 106: 'é', 107: 'M', 108: 'q', 109: 'Й', 110: 'z',
               111: 'S', 112: 'A', 113: 'N', 114: 'j', 115: 'C', 116: 'L', 117: 'B', 118: 'y', 119: 'x', 120: 'P',
               121: 'E', 122: 'D', 123: 'è', 124: 'J', 125: 'w', 126: 'k', 127: 'R', 128: 'à', 129: 'H', 130: 'O',
               131: 'G', 132: 'T', 133: '_', 134: 'Ь', 135: 'ê', 136: 'F', 137: 'K', 138: 'Q', 139: 'Ы', 140: 'W',
               141: 'і', 142: 'U', 143: 'Z', 144: 'ô', 145: 'ç', 146: 'â', 147: 'ó', 148: 'î', 149: 'ü', 150: 'Ё',
               151: 'ѣ', 152: 'º', 153: '½', 154: 'Y', 155: 'ä', 156: 'ù', 157: 'ö', 158: 'œ', 159: 'á', 160: 'û',
               161: '¼', 162: 'є', 163: 'Ъ', 164: 'ï', 165: 'ë', 166: 'ė', 167: 'Ç', 168: 'ß', 169: 'ò', 170: 'ї',
               171: 'ę', 172: 'ў', 173: 'ć', 174: 'ą', 175: 'Š', 176: 'š', 177: 'À', 178: 'ο', 179: 'ś', 180: 'α',
               181: 'β', 182: 'ý', 183: 'ј', 184: '場', 185: '工', 186: '罵', 187: '垢', 188: '馬', 189: '嘔', 190: '婆',
               191: '駆', 192: 'Ü', 193: 'ό', 194: 'ν', 195: 'Ś', 196: 'ż', 197: 'å', 198: 'Ö', 199: 'ł', 200: '⅓',
               201: 'ѕ', 202: 'Ž', 203: 'ž', 204: 'τ', 205: 'í', 206: 'ň', 207: 'Ѕ', 208: 'č', 209: '¾', 210: 'ø',
               211: 'ґ'}

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

def evaluate(model, char_to_idx, idx_to_char, start_text=' ', prediction_len=200, temp=0.3):
    hidden = model.init_hidden()
    idx_input = [char_to_idx[char] for char in start_text]
    train = torch.LongTensor(idx_input).view(-1, 1, 1).to(device)
    predicted_text = start_text

    _, hidden = model(train, hidden)

    inp = train[-1].view(-1, 1, 1)

    for i in range(prediction_len):
        output, hidden = model(inp.to(device), hidden)
        output_logits = output.cpu().data.view(-1)
        p_next = F.softmax(output_logits / temp, dim=-1).detach().cpu().data.numpy()
        top_index = np.random.choice(len(char_to_idx), p=p_next)
        inp = torch.LongTensor([top_index]).view(-1, 1, 1).to(device)
        predicted_char = idx_to_char[top_index]
        predicted_text += predicted_char

    return predicted_text


class TextRNN(nn.Module):

    def __init__(self, input_size, hidden_size, embedding_size, n_layers=1):
        super(TextRNN, self).__init__()

        self.input_size = input_size
        self.hidden_size = hidden_size
        self.embedding_size = embedding_size
        self.n_layers = n_layers

        self.encoder = nn.Embedding(self.input_size, self.embedding_size)
        self.lstm = nn.LSTM(self.embedding_size, self.hidden_size, self.n_layers)
        self.dropout = nn.Dropout(0.2)
        self.fc = nn.Linear(self.hidden_size, self.input_size)

    def forward(self, x, hidden):
        x = self.encoder(x).squeeze(2)
        out, (ht1, ct1) = self.lstm(x, hidden)
        out = self.dropout(out)
        x = self.fc(out)
        return x, (ht1, ct1)

    def init_hidden(self, batch_size=1):
        return (torch.zeros(self.n_layers, batch_size, self.hidden_size, requires_grad=True).to(device),
                torch.zeros(self.n_layers, batch_size, self.hidden_size, requires_grad=True).to(device))


model_path = staticfiles_storage.path('LSTM_model_1_51.pth')

model = TextRNN(input_size=len(idx_to_char), hidden_size=128, embedding_size=128, n_layers=4)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))

model.eval()
