from rest_framework import serializers
from .models import Ad, ExchangeProposal


class AdSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Ad
        fields = [
            "id",
            "user",
            "title",
            "description",
            "image_url",
            "category",
            "condition",
            "created_at",
        ]
        read_only_fields = ["id", "user", "created_at"]


        def create(self, validated_data):
            request = self.context.get("request")
            if request and hasattr(request, "user"):
                validated_data["user"] = request.user
            return super().create(validated_data)


        def validate_title(self, title):
            if not title.strip():
                raise serializers.ValidationError("Title is required")
            return title

        def validate_description(self, description):
            if not description.strip():
                raise serializers.ValidationError("Description is required")
            return description


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeProposal
        fields = [
            "id",
            "ad_sender",
            "ad_receiver",
            "comment",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "status", "created_at"]


    def create(self, validated_data):
        validated_data["status"] = ExchangeProposal.status.PENDING
        return super().create(validated_data)


    def validate(self, data):
        ad_sender = getattr(data, 'ad_sender')
        ad_receiver = getattr(data, 'ad_receiver')
        user = self.context['request'].user
        if ad_sender.user != user:
            raise serializers.ValidationError("You are not the owner of the ad")
        if ad_sender == ad_receiver:
            raise serializers.ValidationError("You can't exchange the same ad")
        return data


