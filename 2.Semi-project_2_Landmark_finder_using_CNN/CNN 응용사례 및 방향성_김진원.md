■ 조 편성  
1조 : 정성훈, 박지원, 이찬주, 이동재, 김동현  
2조 : 이지윤, 이학민, 조원우, 이동진, 박희원  
3조 : 김진원, 노용철, 안애솔, 홍세준, 민채정  
4조(개인) : 안재진, 조유정, 조윤석  

# CNN 

1. Aji, Indra. (2020). Landmark Classification Service Using Convolutional Neural Network and Kubernetes. International Journal of Advanced Trends in Computer Science and Engineering. 9. 2817-2823. 10.30534/ijatcse/2020/52932020. 

   - 에 의하면 가장 좋은 CNN 방법은 ResNet50 모델과 Adamax최적화 방식을 함께 사용하는 것입니다. 정확도 95.67%

   - 구글 Colab을 활용

   - 이미지 전처리시 색인화 진행 (정확도를 높인다.)

2. [ImageNet: VGGNet, ResNet, Inception, and Xception with Keras 사용법](https://www.pyimagesearch.com/2017/03/20/imagenet-vggnet-resnet-inception-xception-keras/)
   
- Even though ResNet is *much* deeper than VGG16 and VGG19, the model size is actually *substantially smaller* due to the usage of global average pooling rather than fully-connected layers — this reduces the model size down to 102MB for ResNet50.
  
3. [ResNet논문 리뷰](https://ganghee-lee.tistory.com/41)

   ![구조](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb5HQOH%2FbtqBNjqRUsk%2FYnxL1ai7kIa9peEYSRlQGK%2Fimg.png)

4. Junayed, Masum Shah & Jeny, Afsana & Neehal, Nafis & Atik, Syeda & Hossain, Syed. (2019). A Comparative Study of Different CNN Models in City Detection Using Landmark Images. 10.1007/978-981-13-9181-1_48. 
   - 방법론: 
     - <img src="CNN 응용사례 및 방향성.assets/method1.png" alt="method1" style="zoom:80%;" />
   - 전처리 방법: 과적합을 방지하기위해 인공적으로 데이터를 증식시킴 -> They are Rotate +30, Rotate -30, Translation, Shearing, and Flip.
   - 5400장의 증식된 이미지를 ResNet50은 총 2일이 걸림. (일반적인 컴퓨터 사양 기준)
5. K. He, X. Zhang, S. Ren and J. Sun, "Deep Residual Learning for Image Recognition," 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, NV, 2016, pp. 770-778, doi: 10.1109/CVPR.2016.90.
   - ResNet 논문에 의하면 사람의 이미지 분류 에러율이 5% 이면 150개의 은닉층을 사용하는 ResNet은 3.5%를 달성
   - 사람보다 더 분류를 잘하게됨

# 응용사례

Image-Net

Alphago



[Pre-trained ResNet50](https://github.com/fchollet/deep-learning-models)

- 트레이닝된 모델에다 추가적으로 랜드마크를 학습하는 방식으로 나아가자.

[Keras Applications](https://keras.io/api/applications/)

- ResNet50 모델 사용법



[참고: 딥러닝 모델](https://deview.kr/data/deview/2019/presentation/[115]어디까지+깎아봤니_모바일+서비스를+위한+가벼운+이미지+인식_검출+딥러닝+모델.pdf)

- [CutMix (ICCV 2019)](https://github.com/clovaai/CutMix-PyTorch) 현존 최고의 Regularization정형화 방법을 사용하면 모델을 더 향상 시킬 수 있다.



# 기획안 추가 방안

- 배달 로봇 또한 이 랜드마크 학습 데이터를 기반으로 정확한 위치 추정을 할 수 있다.

# Image Augmentation

[kakaobrain_데이터 어그먼테이션 연구 동향](https://www.kakaobrain.com/blog/64)

케라스 이미지 data 제너레이터 함수 사용

```python
train_datagen = ImageDataGenerator(rescale=1./255, 
                                   rotation_range=15,
                                   width_shift_range=0.1,
                                   height_shift_range=0.1,
                                   shear_range=0.5,
                                   zoom_range=[0.8, 2.0],
                                   horizontal_flip=True,
                                   vertical_flip=True,
                                   fill_mode='nearest')
train_generator = train_datagen.flow_from_directory(
        'handwriting_shape/train',
        target_size=(24, 24),
        batch_size=3,
        class_mode='categorical')
#파일로 저장하지 않고 이미지 증식이 됨

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
        'handwriting_shape/test2',
        target_size=(24, 24),    
        batch_size=3,
        class_mode='categorical')
```

각각의 모델 생성



ResNet-50

https://eremo2002.tistory.com/76

inception-v3

https://nevfiasco.tistory.com/6

https://sike6054.github.io/blog/paper/third-post/

시간있으면 (Xception)

만들어진 모델에서 테스트 데이터 넣고 나오는 결과값 보여주기

각각의 모델에 대해 채널과,필터와, 클래스 와 히트맵 시각화

분류 해서 값보여주기

구글맵에 표시





- 랜드마크 이미지의 회전은 최대 90.
- 밝기 조절은 오후 시간때도 있으니까 어둡게도 적용하면 좋을 것 같다.
- 상하/좌우 로 이동하는 것도 좋은 생각이다.
- horizontal flip은 필요해보인다 (어쩌다 셀카 설정이 그럴때가 있어서..)



# 폴더 트레인, 테스트, validation

https://gist.github.com/bertcarremans/679624f369ed9270472e37f8333244f5

```python
import splitfolders
split_folders.ratio('Data', output="output", seed=1337, ratio=(.8, 0.1,0.1))
```

### 폴더 나누는 코드

https://pypi.org/project/split-folders/





# 프로젝트 스토리

### 리서치 

- resnet-50, adamax (성능 좋다는 것을 확인)
- 다른 논문들 및 벤치마크

데이터 (랜드마크) -서울시

- 파일 개수 비율 시각화

  전처리

  - 데이터 증식 (개수 100개 로 될때까지)
    - 증식 방법 설명 왜 몇도로 하였고 좌우는 셀카 이유 등등
  - 그래프 시각화 모두 100개 확인 (비슷한 비율)
  - 파일 train, validation, test 로 split (그림?)

### 딥러닝 CNN 학습

- CNN이란? 
  - 우리가 시도해본 State-of-Art의 딥러닝 네트웍은 vgg, inception, resnet
- VGG 구조 요약 (figure)
- inception 구조 요약 (figure)
- Res-Net의 구조 요약 : 왜 랜드마크가 잘나올까? 라는 답이 있는지 찾아보기 (figure)
  - 학습 결과 (그래프)
  - Res-Net의 필터 및 채널 시각화
  - Res-Net을 활용한 모델 예측 및 히트맵 적용

### opencv

로 모델 활용 및 예측된 빌딩을 네모 박스로 표시 + 라벨링

### 서비스 

사진을 통한 위치 서비스 연동 (구글맵)
