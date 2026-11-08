# Verify requirements for g_H_u1-6 questions
import json

def check_q(q):
    assert len(q['options']) == 5, f"{q['id']} does not have 5 options"
    assert 0 <= q['correct_idx'] <= 4, f"{q['id']} invalid correct_idx"
    assert q['options'][q['correct_idx']]['is_correct'] is True, f"{q['id']} correct_idx mismatch"
    assert sum(1 for o in q['options'] if o['is_correct']) == 1, f"{q['id']} multiple correct options"
    assert len(q['stem']) > 40, f"{q['id']} stem too short"
    assert len(q['explanation']) > 40, f"{q['id']} explanation too short"
    
    # Check option length balance
    lens = [len(o['text']) for o in q['options']]
    avg_len = sum(lens) / 5
    corr_len = lens[q['correct_idx']]
    ratio = corr_len / avg_len
    assert 0.65 <= ratio <= 1.5, f"{q['id']} option length imbalance: ratio {ratio:.2f} (corr {corr_len} vs avg {avg_len:.1f})"
    
    # Check parentheses giveaway
    corr_text = q['options'][q['correct_idx']]['text']
    dist_texts = [o['text'] for idx, o in enumerate(q['options']) if idx != q['correct_idx']]
    if '(' in corr_text and ')' in corr_text:
        assert all('(' in d and ')' in d for d in dist_texts), f"{q['id']} parenthetical giveaway in correct option"

print("Validation test function ready.")
