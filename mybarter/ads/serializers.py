from rest_framework import serializers
from .models import Ad, ExchangeProposal


class AdSerializer(serializers.ModelSerializer):
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
