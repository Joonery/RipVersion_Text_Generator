
rand = function(max) {
    return Math.floor(Math.random() * max)
}

get_next_lul = function(str) {
    return (str.charCodeAt(str.length-1) - 0xAC00) % 28 == 0
}

make_str = function(str, is_Lul) {
    start_char = str.slice(0,1)
    if(start_char == '을' || start_char == '를')
        if(is_Lul == false)
            start_char = '을'
        else
            start_char = '를'
    else if(start_char == '이' || start_char == '가')
        if(is_Lul == false)
            start_char = '이'
        else
            start_char = '가'
    else if(start_char == '은' || start_char == '는')
        if(is_Lul == false)
            start_char = '은'
        else
            start_char = '는'
    return start_char + str.slice(1)
}

main = function(start_txt, overlap) {
    
    questions = [
        
    ]

    end_question = [
        
    ]

    return_text = start_txt
    is_Lul = get_next_lul(start_txt)

    var questions_temp = []
    
    while(overlap > 0) {
    
        if(questions_temp.length == 0)
            questions_temp = questions.slice()
        const idx = rand(questions_temp.length)
        return_text = return_text + make_str(questions_temp[idx], is_Lul)
        is_Lul = get_next_lul(questions_temp[idx])
        questions_temp.splice(idx, 1)
        overlap -= 1
    }

    return return_text + make_str(end_question[rand(end_question.length)], is_Lul)
}

window.onload = function() {
    document.getElementById('submit').onclick = function() {
        var start_txt = document.getElementById('start_txt').value
        var overlap = document.getElementById('overlap').valueAsNumber
        document.getElementById('result').textContent = main(start_txt, overlap)
    }
}