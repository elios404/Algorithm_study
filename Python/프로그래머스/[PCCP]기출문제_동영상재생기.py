def solution(video_len, pos, op_start, op_end, commands):
    #시간 관련 문자열을 모두 초로 변환하기
    sec_video_len = int(video_len[0:2])*60 + int(video_len[3:]) 
    sec_pos = int(pos[0:2])*60 + int(pos[3:])
    sec_op_start = int(op_start[0:2])*60 + int(op_start[3:])
    sec_op_end = int(op_end[0:2])*60 + int(op_end[3:])

    for line in commands:
        #처음에 오프닝 확인
        if sec_pos >= sec_op_start and sec_pos <= sec_op_end:
            sec_pos = sec_op_end

        #커맨드에 따라 이동
        if line == "next":
            sec_pos += 10
        elif line == "prev":
            sec_pos -= 10

        #동영상의 처음이나 끝을 보정
        if sec_pos < 0:
            sec_pos = 0
        elif sec_pos > sec_video_len:
            sec_pos = sec_video_len

        #오프닝 안에 있는지 다시 확인
        if sec_pos >= sec_op_start and sec_pos <= sec_op_end:
            sec_pos = sec_op_end

    mm_pos = sec_pos // 60
    ss_pos = sec_pos % 60

    answer = "{:02}".format(mm_pos) + ":" + "{:02}".format(ss_pos)

    return answer

'''
이것을 통해 배운 점

다른 사람들의 해답을 보니 비슷한 부분을 함수 처리한 것이 인상 깊었다.
시간으로 주어진 문자열을 초로 변환할 때 함수를 활용할 수 있었을 것이다.

또한 어떤 기능을 하는 것을 함수로 만들 수 있다. 마지막에 초를 다시 시간 문자열로 
전환하는 것 또한 한 번 밖에 나타나지 않지만, 특정 기능을 수행하기에 함수로 만들 수 있다.

또한 문자열 포맷을 정하는 것을 배웠다
"{:02}".format(변수) 를 통해서 문자열의 포맷을 정해줄 수 있었다.

'''