from . import generate


def three_paths(my_string, temperature=0.6, pred_length=400):
    generated_message_1 = generate.evaluate(
        generate.model,
        generate.char_to_idx,
        generate.idx_to_char,
        temp=temperature,
        prediction_len=pred_length,
        start_text=my_string
    )

    generated_message_2 = generate.evaluate(
        generate.model,
        generate.char_to_idx,
        generate.idx_to_char,
        temp=temperature,
        prediction_len=pred_length,
        start_text=my_string
    )

    generated_message_3 = generate.evaluate(
        generate.model,
        generate.char_to_idx,
        generate.idx_to_char,
        temp=temperature,
        prediction_len=pred_length,
        start_text=my_string
    )

    return [generated_message_1, generated_message_2, generated_message_3]