<template>
	<view class="container">
		<view class="sa-article">
			<view>{{content}}</view>
		</view>
	</view>
</template>
<script>
	export default {
		data() {
			return {
				barBack: getApp().globalData.barBack,
				barColor: getApp().globalData.barColor,
				isLoader: true,
				title: '',
				content: ''
			};
		},
		onLoad(e) {
			this.getArticle(e.id);
		},
		methods: {
			getArticle(id) {
				if(id == 1) {
					this.content = '添加到桌面';
				}else{
					this.content = '关于我们';
				}
			}
		}
	}
</script>
<style lang="less">
	page {
		background-color: #fff;
	}
	.sa-article {
		font-size: 32rpx;
		padding: 30rpx;
	}
</style>